"""add phonenumber to customers

Revision ID: c5c407bd7c0f
Revises: 02a75d2d3dd7
Create Date: 2024-08-22 16:34:44.021543

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c5c407bd7c0f'
down_revision: Union[str, None] = '02a75d2d3dd7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.add_column('customers', sa.Column('phonenumber', sa.String(20), nullable=True))

def downgrade() -> None:
    op.drop_column('customers', 'phonenumber')