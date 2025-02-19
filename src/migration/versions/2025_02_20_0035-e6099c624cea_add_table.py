"""add table

Revision ID: e6099c624cea
Revises: 
Create Date: 2025-02-20 00:35:49.136185

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e6099c624cea'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_event', sa.String(), nullable=False),
    sa.Column('date', sa.String(), nullable=False),
    sa.Column('time', sa.String(), nullable=False),
    sa.Column('location', sa.String(), nullable=False),
    sa.Column('limit_people', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('events')
    # ### end Alembic commands ###
