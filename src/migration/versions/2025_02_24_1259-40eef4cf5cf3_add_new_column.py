"""add new column

Revision ID: 40eef4cf5cf3
Revises: e4b75f66ad30
Create Date: 2025-02-24 12:59:38.947119

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '40eef4cf5cf3'
down_revision: Union[str, None] = 'e4b75f66ad30'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('visitors', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_unique_constraint(None, 'visitors', ['user_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'visitors', type_='unique')
    op.drop_column('visitors', 'user_id')
    # ### end Alembic commands ###
