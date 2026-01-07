from alembic import op
import sqlalchemy as sa

revision = 'NEW_REVISION_ID'
down_revision = '55e75f7a1a85'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'posts',
        sa.Column(
            'published',
            sa.Boolean(),
            nullable=False,
            server_default='TRUE'
        )
    )


def downgrade():
    op.drop_column('posts', 'published')
