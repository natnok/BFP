"""add hotel table

Revision ID: 7a0de1100378
Revises:
Create Date: 2026-07-12 13:14:21.754651

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "7a0de1100378"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "hotel",
        sa.Column("hotel_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=1000), nullable=False),
        sa.Column("description", sa.String(length=10000), nullable=False),
        sa.Column("stars", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("hotel_id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("hotel")
