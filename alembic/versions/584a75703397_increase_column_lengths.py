"""increase column lengths

Revision ID: 584a75703397
Revises: 41d1a5e01aab
Create Date: 2024-08-22 16:56:54.008300

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '584a75703397'
down_revision: Union[str, None] = '41d1a5e01aab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.alter_column('customers', 'name', type_=sa.String(length=100))
    op.alter_column('customers', 'notes', type_=sa.String(length=100))
    op.alter_column('customers', 'streetaddress', type_=sa.String(length=100))
    op.alter_column('customers', 'email', type_=sa.String(length=100))

def downgrade() -> None:
    op.alter_column('customers', 'name', type_=sa.String(length=20))
    op.alter_column('customers', 'notes', type_=sa.String(length=20))
    op.alter_column('customers', 'streetaddress', type_=sa.String(length=20))
    op.alter_column('customers', 'email', type_=sa.String(length=20))