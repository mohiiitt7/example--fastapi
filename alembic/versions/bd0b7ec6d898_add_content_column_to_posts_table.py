"""add content column to posts table

Revision ID: bd0b7ec6d898
Revises: cff5d38f395d
Create Date: 2026-01-06 19:48:30.894851

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd0b7ec6d898'
down_revision: Union[str, Sequence[str], None] = 'cff5d38f395d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
