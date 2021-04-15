"""empty message

Revision ID: 1096f777d330
Revises: f82bce32e1df
Create Date: 2021-04-15 16:01:33.100583

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1096f777d330'
down_revision = 'f82bce32e1df'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('account', 'date_created', type_=sa.DateTime(), existing_type=sa.Date())
    op.alter_column('account', 'most_recent_login', type_=sa.DateTime(), existing_type=sa.Date())


def downgrade():
    op.alter_column('account', 'date_created', type_=sa.Date(), existing_type=sa.DateTime())
    op.alter_column('account', 'most_recent_login', type_=sa.Date(), existing_type=sa.DateTime())
