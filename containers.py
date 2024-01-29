from dependency_injector import containers, providers
from user.application.user_service import UserService
from note.application.note_service import NoteService

from user.infra.repository.user_repo import UserRepository
from note.infra.repository.note_repo import NoteRepository


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=[
            "user",
            "note",
        ],
    )

    user_repo = providers.Factory(UserRepository)
    user_service = providers.Factory(UserService, user_repo=user_repo)
    note_repo = providers.Factory(NoteRepository)
    note_service = providers.Factory(NoteService, note_repo=note_repo)
