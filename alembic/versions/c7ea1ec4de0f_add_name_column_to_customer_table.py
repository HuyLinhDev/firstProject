"""Add name column to Customer Table

Revision ID: c7ea1ec4de0f
Revises: 584a75703397
Create Date: 2024-09-05 17:05:30.584982

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7ea1ec4de0f'
down_revision: Union[str, None] = '584a75703397'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('customers', sa.Column('name', sa.String(20), nullable=True))


def downgrade() -> None:
    op.drop_column('customers', 'name')
