"""create_user_model

Revision ID: c0e120e6eeba
Revises: 
Create Date: 2023-12-18 14:55:10.381593

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "c0e120e6eeba"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer()),
        sa.Column("username", sa.String(length=200), nullable=False),
        sa.Column("first_name", sa.String(length=100)),
        sa.Column("last_name", sa.String(length=1000)),
        sa.Column("password", sa.VARCHAR(length=500)),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_column("users")
