"""empty message

Revision ID: f82bce32e1df
Revises: 08c0da289311
Create Date: 2021-04-15 15:47:57.856263

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f82bce32e1df'
down_revision = '08c0da289311'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('most_recent_login', sa.Date(), nullable=True))
    op.drop_column('account', 'fbid')


def downgrade():
    op.add_column('account', sa.Column('fbid', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
    op.drop_column('account', 'most_recent_login')
