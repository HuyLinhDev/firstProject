"""add field name

Revision ID: 41d1a5e01aab
Revises: 4b87f85d1ac6
Create Date: 2024-08-22 16:55:08.456236

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '41d1a5e01aab'
down_revision: Union[str, None] = '4b87f85d1ac6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.add_column('customers', sa.Column('name', sa.String(length=100), nullable=True))

def downgrade() -> None:
    op.drop_column('customers', 'name')
