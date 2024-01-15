from datetime import datetime
from ulid import ULID
from note.domain.note import Note, Tag
from note.domain.repository.note_repo import INoteRepository


class NoteService:
    def __init__(
        self,
        note_repo: INoteRepository,
    ):
        self.note_repo = note_repo
        self.ulid = ULID()

    def get_notes(
        self,
        user_id: str,
        page: int,
        items_per_page: int,
    ) -> tuple[int, list[Note]]:
        return self.note_repo.get_notes(
            user_id=user_id,
            page=page,
            items_per_page=items_per_page,
        )

    def get_notes_by_tag(
        self,
        user_id: str,
        tag_name: str,
        page: int,
        items_per_page: int,
    ) -> tuple[int, list[Note]]:
        return self.note_repo.get_notes_by_tag_name(
            user_id=user_id,
            tag_name=tag_name,
            page=page,
            items_per_page=items_per_page,
        )

    def get_note(self, user_id: str, id: str) -> Note:
        return self.note_repo.find_by_id(user_id, id)

    def create_note(
        self,
        user_id: str,
        title: str,
        content: str,
        memo_date: str,
        tag_names: list[str] = [],
    ) -> Note:
        now = datetime.now()

        tags = [
            Tag(
                id=self.ulid.generate(),
                name=title,
                updated_at=now,
                created_at=now,
            )
            for title in tag_names
        ]

        note = Note(
            id=self.ulid.generate(),
            user_id=user_id,
            title=title,
            content=content,
            memo_date=memo_date,
            tags=tags,
            created_at=now,
            updated_at=now,
        )

        self.note_repo.save(user_id, note)

        return note

    def update_note(
        self,
        user_id: str,
        id: str,
        title: str | None = None,
        content: str | None = None,
        memo_date: str | None = None,
        tag_names: list[str] | None = [],
    ) -> Note:
        note = self.note_repo.find_by_id(user_id, id)
        if title:
            note.title = title
        if content:
            note.content = content
        if memo_date:
            note.memo_date = memo_date
        if tag_names is not None:
            now = datetime.now()
            note.tags = [
                Tag(
                    id=self.ulid.generate(),
                    name=title,
                    created_at=now,
                    updated_at=now,
                )
                for title in tag_names
            ]

        return self.note_repo.update(user_id, note)

    def delete_note(self, user_id: str, id: str):
        return self.note_repo.delete(user_id, id)
