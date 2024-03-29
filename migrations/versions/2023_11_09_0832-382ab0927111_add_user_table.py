"""add User Table

Revision ID: 382ab0927111
Revises:
Create Date: 2024-01-15 23:35:56.048802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '382ab0927111'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'User',
        sa.Column('id', sa.String(length=36), nullable=False),
        sa.Column('name', sa.String(length=32), nullable=False),
        sa.Column('email', sa.String(length=64), nullable=False),
        sa.Column('password', sa.String(length=64), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('User')
    # ### end Alembic commands ###
