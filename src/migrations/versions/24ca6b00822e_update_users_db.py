"""update_users_db

Revision ID: 24ca6b00822e
Revises: c0e120e6eeba
Create Date: 2023-12-18 17:35:22.516845

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '24ca6b00822e'
down_revision: Union[str, None] = 'c0e120e6eeba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "users",
        "first_name",
        type_=sa.String(200),
        nullable=False
    )
    op.alter_column(
        "users",
        "last_name",
        type_=sa.String(200),
        nullable=False
    )
    op.alter_column(
        "users",
        "password",
        type_=sa.String(200),
        nullable=False
    )
    op.add_column(
        "users",
        sa.Column("last_login", sa.String(200))
    )


def downgrade() -> None:
    pass
