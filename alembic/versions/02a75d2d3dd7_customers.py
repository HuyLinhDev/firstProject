"""customers

Revision ID: 02a75d2d3dd7
Revises: 
Create Date: 2024-08-22 16:30:10.436389

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02a75d2d3dd7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        'customers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('firstname', sa.String(20), nullable=False),
        sa.Column('lastname', sa.String(20), nullable=False),
        sa.Column('accounttype', sa.String(50), nullable=False),
        sa.Column('customerstatus', sa.String(50), nullable=False),
        sa.Column('customersince', sa.String(20), nullable=False),
        sa.Column('country', sa.String(20), nullable=False),
        sa.Column('notes', sa.String(20), nullable=False),
        sa.Column('preferredcontactmethod', sa.String(20), nullable=False),
        sa.Column('email', sa.String(20), nullable=False),
        sa.Column('state', sa.String(20), nullable=False),
        sa.Column('streetaddress', sa.String(20), nullable=False),
        sa.Column('postalcode', sa.String(20), nullable=False),
        sa.Column('city', sa.String(20), nullable=False),
    )

def downgrade() -> None:
    op.drop_table('customers')
