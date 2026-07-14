"""add room table

Revision ID: ae6643a63894
Revises: 7a0de1100378
Create Date: 2026-07-12 13:15:07.166325

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "ae6643a63894"
down_revision: Union[str, Sequence[str], None] = "7a0de1100378"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "room",
        sa.Column("room_id", sa.Integer(), nullable=False),
        sa.Column("number", sa.Integer(), nullable=False),
        sa.Column("description", sa.String(length=10000), nullable=False),
        sa.PrimaryKeyConstraint("room_id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("room")
