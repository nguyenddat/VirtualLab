import json

from sqlalchemy import or_
from sqlalchemy import func
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.device import Device
from app.models.vertex import Vertex
from app.models.connection import Connection
from app.models.experiment import Experiment
from app.models.experiment_device import Experiment_Device
from app.database.init_db import get_db
from app.schemas.experiment.save_experiment import CreateExperimentRequest, CreateExperimentDeviceRequest, UpdateExperimentRequest

router = APIRouter()

@router.get('')
def get_experiment(db: Session = Depends(get_db)):
    experiments = db.query(Experiment).all()
    return [{
        "id":e.id, 
        "name":e.name, 
        "description":e.description,
        "status":e.status,
        "public_status":e.public_status,
        "chapter_id":e.chapter_id,
        "created_by":e.created_by} for e in experiments]


@router.get('/{experiment_id}')
def get_experiment_circuit(experiment_id: int, db: Session = Depends(get_db)):
    devices = []
    connections = []

    exp_devices = db.query(Experiment_Device).filter(Experiment_Device.experiment_id == experiment_id).all()
    for device in exp_devices:
        device_name = device.device_name
        device_type = db.query(Device).filter(Device.id == device.device_id).first().type
        device_properties = device.properties

        start_vertex = db.query(Vertex).filter(Vertex.experiment_device_id == device.id, Vertex.type == "start").first()
        if start_vertex:
            start_conn = db.query(Connection).filter(
                or_(
                    Connection.vertex_1_id == start_vertex.id,
                    Connection.vertex_2_id == start_vertex.id
                )
            ).first()
            if start_conn:
                # Tìm partner vertex (không phải vertex hiện tại)
                if start_conn.vertex_1_id == start_vertex.id:
                    partner_vertex_id = start_conn.vertex_2_id
                else:
                    partner_vertex_id = start_conn.vertex_1_id
                
                partner = db.query(Vertex).filter(Vertex.id == partner_vertex_id).first()
                if partner:
                    partner_device = db.query(Experiment_Device).filter(Experiment_Device.id == partner.experiment_device_id).first()
                    if partner_device:
                        # Chỉ thêm connection nếu device_name hiện tại < partner_device.device_name để tránh trùng lặp
                        if device_name < partner_device.device_name:
                            connections.append([f"{device_name}.start", f"{partner_device.device_name}.{partner.type}"])

        end_vertex = db.query(Vertex).filter(Vertex.experiment_device_id == device.id, Vertex.type == "end").first()
        if end_vertex:
            end_conn = db.query(Connection).filter(
                or_(
                    Connection.vertex_1_id == end_vertex.id,
                    Connection.vertex_2_id == end_vertex.id
                )
            ).first()
            if end_conn:
                # Tìm partner vertex (không phải vertex hiện tại)
                if end_conn.vertex_1_id == end_vertex.id:
                    partner_vertex_id = end_conn.vertex_2_id
                else:
                    partner_vertex_id = end_conn.vertex_1_id
                
                partner = db.query(Vertex).filter(Vertex.id == partner_vertex_id).first()
                if partner:
                    partner_device = db.query(Experiment_Device).filter(Experiment_Device.id == partner.experiment_device_id).first()
                    if partner_device:
                        # Chỉ thêm connection nếu device_name hiện tại < partner_device.device_name để tránh trùng lặp
                        if device_name < partner_device.device_name:
                            connections.append([f"{device_name}.end", f"{partner_device.device_name}.{partner.type}"])
        
        devices.append({
            "name": device_name,
            "type": device_type,
            "properties": device_properties,
            "start_vertex": [start_vertex.x, start_vertex.y],
            "end_vertex": [end_vertex.x, end_vertex.y]
        })
    response = {
        "devices": devices,
        "connections": connections
    }
    print(response)
    return response


@router.get("/user/{user_id}")
def get_experiment_by_user_id(
    user_id: int,
    db: Session = Depends(get_db),
    offset: int = 0,
    limit: int = 10
):
    experiments = db.query(Experiment).filter(Experiment.created_by == user_id).offset(offset).limit(limit).all()
    return [{
        "id":e.id, 
        "name":e.name,
        "description":e.description,
        "status":e.status,
        "public_status":e.public_status,
        "chapter_id":e.chapter_id,
        "created_by":e.created_by
    } for e in experiments]


@router.post("/user/{user_id}")
def create_experiment(
    user_id: int,
    request: CreateExperimentRequest,
    db: Session = Depends(get_db)
):
    try:
        experiment = Experiment(
            name=request.name,
            status=request.status,
            public_status=request.public_status,
            description=request.description or "",
            chapter_id=request.chapter_id,
            created_by=user_id,
        )
        db.add(experiment)
        db.commit()
        db.refresh(experiment)
        return {"message": "Experiment created successfully"}
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/user/{user_id}/basic")
def update_basic_info(
    user_id: int,
    request: UpdateExperimentRequest,
    db: Session = Depends(get_db)
):
    try:
        experiment = db.query(Experiment).filter(Experiment.id == request.experiment_id).first()
        if not experiment:
            raise HTTPException(status_code=404, detail="Experiment not found")
        experiment.name = request.name
        experiment.description = request.description or ""
        experiment.status = request.status
        experiment.public_status = request.public_status
        db.commit()
        db.refresh(experiment)
        return {"message": "Experiment updated successfully"}
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/user/{user_id}/device")
def create_experiment_device(
    request: CreateExperimentDeviceRequest,
    db: Session = Depends(get_db)
):
    print(request.devices)
    print(request.connections)
    print(request.experiment_id)
    """Xóa toàn bộ dữ liệu cũ"""
    existed_devices = db.query(Experiment_Device).filter(Experiment_Device.experiment_id == request.experiment_id).all()
    for device in existed_devices:
        start_vertex = db.query(Vertex).filter(Vertex.experiment_device_id == device.id, Vertex.type == "start").first()
        end_vertex = db.query(Vertex).filter(Vertex.experiment_device_id == device.id, Vertex.type == "end").first()

        start_conn = db.query(Connection).filter(
            or_(
                Connection.vertex_1_id == start_vertex.id,
                Connection.vertex_2_id == start_vertex.id
            )
        ).first()
        end_conn = db.query(Connection).filter(
            or_(
                Connection.vertex_1_id == end_vertex.id,
                Connection.vertex_2_id == end_vertex.id
            )
        ).first()
        for x in [end_conn, start_conn, start_vertex, end_vertex]:
            try:
                db.delete(x)
            except:
                continue
        db.delete(device)
    
    vertex_map = {}
    devices = request.devices
    connections = request.connections
    for device in devices:
        device_type = db.query(Device).filter(
            func.lower(Device.type) == device["type"].lower()
        ).first()
        
        new_device = Experiment_Device(
            experiment_id=request.experiment_id,
            device_name=device["name"],
            device_id=device_type.id,
            properties=json.dumps(device["properties"], ensure_ascii=False),
        )
        db.add(new_device)
        db.flush()


        start_vertex = Vertex(
            experiment_device_id=new_device.id,
            type="start",
            x=device["startVertex"][0],
            y=device["startVertex"][1]
        )
        db.add(start_vertex)
        db.flush()


        end_vertex = Vertex(
            experiment_device_id=new_device.id,
            type="end",
            x=device["endVertex"][0],
            y=device["endVertex"][1]
        )
        db.add(end_vertex)
        db.flush()

        vertex_map[f"{device['name']}"] = {
            "startvertex": start_vertex.id,
            "endvertex": end_vertex.id
        }
    db.commit()

    for conn in connections:
        device_a, vertex_a = conn[0].split(".")
        device_b, vertex_b = conn[1].split(".")

        vertex_a = vertex_map[device_a][vertex_a]
        vertex_b = vertex_map[device_b][vertex_b]
        new_conn = Connection(
            vertex_1_id=vertex_a,
            vertex_2_id=vertex_b
        )
        db.add(new_conn)

    db.commit()
    return {"message": "Devices and connections updated successfully"}