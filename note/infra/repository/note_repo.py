from note.domain.note import Note
from note.domain.repository.note_repo import INoteRepository


class NoteRepository(INoteRepository):
    def get_notes(
        self,
        user_id: str,
        page: int,
        items_per_page: int,
    ) -> tuple[int, list[Note]]:
        raise NotImplementedError

    def find_by_id(self, user_id: str, id: str) -> Note:
        raise NotImplementedError

    def save(self, user_id: str, note: Note) -> Note:
        raise NotImplementedError

    def update(self, user_id: str, note: Note) -> Note:
        raise NotImplementedError

    def delete(self, user_id: str, id: str):
        raise NotImplementedError

    def delete_tags(self, user_id: str, id: str):
        raise NotImplementedError

    def get_notes_by_tag_name(
        self,
        user_id: str,
        tag_name: str,
        page: int,
        items_per_page: int,
    ) -> tuple[int, list[Note]]:
        raise NotImplementedError
