"""remove id, add customerid

Revision ID: 4b87f85d1ac6
Revises: c5c407bd7c0f
Create Date: 2024-08-22 16:53:26.533290

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b87f85d1ac6'
down_revision: Union[str, None] = 'c5c407bd7c0f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    op.drop_column('customers', 'id')
    op.add_column('customers', sa.Column('customerid', sa.Integer, primary_key=True))

def downgrade() -> None:
    op.add_column('customers', sa.Column('id', sa.Integer, primary_key=True))
    op.drop_column('customers', 'customerid')