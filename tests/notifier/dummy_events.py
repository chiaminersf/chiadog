# project
import os
from src.notifier import Event, EventType, EventPriority, EventService


class DummyEvents:
    @staticmethod
    def get_low_priority_events():
        machine_name = os.uname()[1]
        return [
            Event(
                type=EventType.USER,
                priority=EventPriority.LOW,
                service=EventService.HARVESTER,
                message=f"Low priority notification 1 in {machine_name}.",
            ),
            Event(
                type=EventType.USER,
                priority=EventPriority.LOW,
                service=EventService.HARVESTER,
                message=f"Low priority notification 2 in {machine_name}.",
            ),
        ]

    @staticmethod
    def get_normal_priority_events():
        machine_name = os.uname()[1]
        return [
            Event(
                type=EventType.USER,
                priority=EventPriority.NORMAL,
                service=EventService.HARVESTER,
                message=f"Normal priority notification 1 in {machine_name}.",
            ),
        ]

    @staticmethod
    def get_high_priority_events():
        machine_name = os.uname()[1]
        return [
            Event(
                type=EventType.USER,
                priority=EventPriority.HIGH,
                service=EventService.HARVESTER,
                message=f"High priority notification 1 in {machine_name}.",
            ),
        ]
