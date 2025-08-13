from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_

from models.device import Device
from models.vertex import Vertex
from models.connection import Connection
from models.experiment import Experiment
from models.experiment_device import Experiment_Device
from database.init_db import get_db

router = APIRouter()

@router.get('')
def get_experiment(db: Session = Depends(get_db)):
    experiments = db.query(Experiment).all()
    return [{"id":e.id, "name":e.name, "chapter_id":e.chapter_id} for e in experiments]


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