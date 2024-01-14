from dependency_injector import containers, providers

# from user.infra.repository.user_repo import UserRepository


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["user.application"])

    # user_repo = providers.Factory(UserRepository)
    user_repo = providers.Singleton(
        "user.infra.repository.user_repo.UserRepository",
    )
    user_service = providers.Factory(
        "user.application.user_service.UserService",
        user_repo=user_repo,
    )
