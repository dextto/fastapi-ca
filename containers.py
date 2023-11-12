from dependency_injector import containers, providers

from user.infra.repository.user_repo import UserRepository


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["user.application"])

    user_repo = providers.Factory(UserRepository)
