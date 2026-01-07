"""add foreign-key to posts table

Revision ID: 55e75f7a1a85
Revises: 8717eb749b8b
Create Date: 2026-01-07 11:40:59.667625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '55e75f7a1a85'
down_revision: Union[str, Sequence[str], None] = '8717eb749b8b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Step 1: add column (nullable for safety)
    op.add_column(
        'posts',
        sa.Column('owner_id', sa.Integer(), nullable=True)
    )

    # Step 2: add foreign key constraint
    op.create_foreign_key(
        'post_users_fk',
        'posts',
        'users',
        ['owner_id'],
        ['id'],
        ondelete='CASCADE'
    )


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
