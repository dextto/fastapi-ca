from abc import ABCMeta, abstractmethod
from note.domain.note import Note


class INoteRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_notes(
        self,
        user_id: str,
        page: int,
        items_per_page: int,
    ) -> tuple[int, list[Note]]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, user_id: str, id: str) -> Note:
        raise NotImplementedError

    @abstractmethod
    def save(self, user_id: str, note: Note) -> Note:
        raise NotImplementedError

    @abstractmethod
    def update(self, user_id: str, note: Note) -> Note:
        raise NotImplementedError

    @abstractmethod
    def delete(self, user_id: str, id: str):
        raise NotImplementedError

    @abstractmethod
    def delete_tags(self, user_id: str, id: str):
        raise NotImplementedError

    @abstractmethod
    def get_notes_by_tag_name(
        self,
        user_id: str,
        tag_name: str,
        page: int,
        items_per_page: int,
    ) -> tuple[int, list[Note]]:
        raise NotImplementedError
