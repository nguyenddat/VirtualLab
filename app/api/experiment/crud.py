# from typing import List, Optional
# import json
# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from typing import List, Optional
# import json

# from app.database.init_db import get_db
# from schemas import SaveExperimentRequest
# from app.schemas.experiment.responses import (
#     ExperimentResponse, 
#     ExperimentsListResponse, 
#     SaveExperimentResponse, 
#     DeleteExperimentResponse
# )
# from models import Device, Experiment, Experiment_Device, Vertex, Connection

# router = APIRouter()


# @router.post("/create", response_model=SaveExperimentResponse)
# def create_experiment(

#     circuit: SaveExperimentRequest,
#     db: Session = Depends(get_db)
# ):
#     """
#     Save or update an experiment with devices and connections
#     """
#     try:
#         chapter_id = circuit.chapter_id
#         devices = circuit.devices
#         connections = circuit.connections

#         new_experiment = Experiment(
#             chapter_id=chapter_id,
#             name=f"Experiment {chapter_id}",
#             content="Testing create experiment",
#             description="Circuit experiment"
#         )
#         db.add(new_experiment)
#         db.commit()
#         db.refresh(new_experiment)
#         experiment_id = new_experiment.id

#         # Check if experiment exists
#         for device in devices:
#             device_type = device.type
#             properties = device.properties.copy()  # Create a copy to avoid modifying original
            
#             # Extract start_vertex and end_vertex from properties if they exist
#             start_vertex = properties.pop("startVertex", None)
#             end_vertex = properties.pop("endVertex", None)
            
#             # Add vertex information to properties if they exist
#             if start_vertex:
#                 properties["start_vertex"] = start_vertex
#             if end_vertex:
#                 properties["end_vertex"] = end_vertex

#             # Check device type & get device id
#             check_type = db.query(Device).filter(Device.type == device_type).first()
#             if check_type is None:
#                 new_device = Device(type=device_type)
#                 db.add(new_device)
#                 db.commit()
#                 db.refresh(new_device)
#                 device_id = new_device.id
#             else:
#                 device_id = check_type.id        

#             # Create experiment device
#             new_experiment_device = Experiment_Device(
#                 experiment_id=experiment_id, 
#                 device_id=device_id, 
#                 properties=properties
#             )
#             db.add(new_experiment_device)
#             db.commit()
#             db.refresh(new_experiment_device)
        
#         for connection in connections:
#             device_name_1, vertex_1 = connection[0].split("-")
#             device_name_2, vertex_2 = connection[1].split("-")

#             device_1 = db.query(Experiment_Device).filter(Experiment_Device.device_name == device_name_1).first()
#             device_2 = db.query(Experiment_Device).filter(Experiment_Device.device_name == device_name_2).first()

#             new_vertex_1 = Vertex(
#                 x=vertex_1[0],
#                 y=vertex_1[1],
#                 experiment_device_id=device_1.id
#             )
#             db.add(new_vertex_1)
#             db.commit()

#             new_vertex_2 = Vertex(
#                 x=vertex_2[0],
#                 y=vertex_2[1],
#                 experiment_device_id=device_2.id
#             )
#             db.add(new_vertex_2)
#             db.commit()

#             new_connection = Connection(
#                 vertex_1_id=new_vertex_1.id,
#                 vertex_2_id=new_vertex_2.id
#             )
#             db.add(new_connection)
#             db.commit()

#         return {
#             "message": "Experiment saved successfully",
#             "experiment_id": experiment_id,
#             "devices_count": len(devices),
#             "connections_count": len(connections)
#         }
    
#     except Exception as e:
#         db.rollback()
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"Error saving experiment: {str(e)}"
#         )


# @router.get("/{experiment_id}", response_model=ExperimentResponse)
# def get_experiment(experiment_id: int, db: Session = Depends(get_db)):
#     """
#     Get experiment by ID with all its devices and properties
#     """
#     try:
#         # Get experiment
#         experiment = db.query(Experiment).filter(Experiment.id == experiment_id).first()
#         if not experiment:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 detail=f"Experiment with ID {experiment_id} not found"
#             )

#         # Get experiment devices with device information
#         experiment_devices = db.query(Experiment_Device).filter(
#             Experiment_Device.experiment_id == experiment_id
#         ).all()

#         devices = []
#         for exp_device in experiment_devices:
#             device = db.query(Device).filter(Device.id == exp_device.device_id).first()
#             if device:
#                 device_data = {
#                     "name": f"{device.type}-{exp_device.id}",  # Generate name based on type and ID
#                     "type": device.type,
#                     "properties": exp_device.properties
#                 }
#                 devices.append(device_data)

#         # Try to parse connections from experiment content
#         connections = []
#         try:
#             if experiment.content:
#                 content_data = json.loads(experiment.content)
#                 connections = content_data.get("connections", [])
#         except:
#             connections = []

#         return {
#             "experiment_id": experiment.id,
#             "name": experiment.name,
#             "description": experiment.description,
#             "devices": devices,
#             "connections": connections,
#             "created_at": experiment.created_at,
#             "updated_at": experiment.updated_at
#         }
    
#     except HTTPException:
#         raise
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"Error retrieving experiment: {str(e)}"
#         )


# @router.get("/", response_model=ExperimentsListResponse)
# def get_all_experiments(
#     skip: int = 0, 
#     limit: int = 100, 
#     db: Session = Depends(get_db)
# ):
#     """
#     Get all experiments with pagination
#     """
#     try:
#         experiments = db.query(Experiment).offset(skip).limit(limit).all()
        
#         result = []
#         for experiment in experiments:
#             # Count devices for this experiment
#             device_count = db.query(Experiment_Device).filter(
#                 Experiment_Device.experiment_id == experiment.id
#             ).count()
            
#             result.append({
#                 "id": experiment.id,
#                 "name": experiment.name,
#                 "description": experiment.description,
#                 "device_count": device_count,
#                 "created_at": experiment.created_at,
#                 "updated_at": experiment.updated_at
#             })
        
#         return {
#             "experiments": result,
#             "total": len(result),
#             "skip": skip,
#             "limit": limit
#         }
    
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"Error retrieving experiments: {str(e)}"
#         )


# @router.put("/{experiment_id}", response_model=SaveExperimentResponse)
# def update_experiment(
#     experiment_id: int,
#     circuit: SaveExperimentRequest,
#     db: Session = Depends(get_db)
# ):
#     """
#     Update an existing experiment
#     """
#     try:
#         # Check if experiment exists
#         experiment = db.query(Experiment).filter(Experiment.id == experiment_id).first()
#         if not experiment:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 detail=f"Experiment with ID {experiment_id} not found"
#             )

#         # Update experiment content
#         experiment.content = json.dumps({
#             "devices": [device.dict() for device in circuit.devices], 
#             "connections": circuit.connections
#         })
        
#         # Clear existing experiment devices
#         db.query(Experiment_Device).filter(Experiment_Device.experiment_id == experiment_id).delete()
        
#         # Process devices (same logic as save)
#         for device in circuit.devices:
#             device_type = device.type
#             properties = device.properties.copy()
            
#             start_vertex = properties.pop("startVertex", None)
#             end_vertex = properties.pop("endVertex", None)
            
#             if start_vertex:
#                 properties["start_vertex"] = start_vertex
#             if end_vertex:
#                 properties["end_vertex"] = end_vertex

#             check_type = db.query(Device).filter(Device.type == device_type).first()
#             if check_type is None:
#                 new_device = Device(type=device_type)
#                 db.add(new_device)
#                 db.commit()
#                 db.refresh(new_device)
#                 device_id = new_device.id
#             else:
#                 device_id = check_type.id        

#             new_experiment_device = Experiment_Device(
#                 experiment_id=experiment_id, 
#                 device_id=device_id, 
#                 properties=properties
#             )
#             db.add(new_experiment_device)

#         db.commit()

#         return {
#             "message": "Experiment updated successfully",
#             "experiment_id": experiment_id,
#             "devices_count": len(circuit.devices),
#             "connections_count": len(circuit.connections)
#         }
    
#     except HTTPException:
#         raise
#     except Exception as e:
#         db.rollback()
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"Error updating experiment: {str(e)}"
#         )


# @router.delete("/{experiment_id}", response_model=DeleteExperimentResponse)
# def delete_experiment(experiment_id: int, db: Session = Depends(get_db)):
#     """
#     Delete an experiment and all its associated data
#     """
#     try:
#         # Check if experiment exists
#         experiment = db.query(Experiment).filter(Experiment.id == experiment_id).first()
#         if not experiment:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 detail=f"Experiment with ID {experiment_id} not found"
#             )

#         # Delete associated experiment devices
#         db.query(Experiment_Device).filter(Experiment_Device.experiment_id == experiment_id).delete()
        
#         # Delete the experiment
#         db.delete(experiment)
#         db.commit()

#         return {
#             "message": "Experiment deleted successfully",
#             "experiment_id": experiment_id
#         }
    
#     except HTTPException:
#         raise
#     except Exception as e:
#         db.rollback()
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"Error deleting experiment: {str(e)}"
#         )


