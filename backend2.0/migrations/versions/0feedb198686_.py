"""empty message

Revision ID: 0feedb198686
Revises: 0f7ce1ed9fe2
Create Date: 2020-12-04 12:01:20.063732

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.schema import Sequence, CreateSequence


# revision identifiers, used by Alembic.
revision = '0feedb198686'
down_revision = '0f7ce1ed9fe2'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('meal_log')
    op.execute(CreateSequence(Sequence('log_id_seq')))
    op.create_table(
        'meal_log',
        sa.Column('meal_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('log_id', sa.Integer(), Sequence('log_id_seq'), nullable=False),
        sa.Column('raw_text', sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(
            ['meal_id'],
            ['meal.id'],
        ),
        sa.PrimaryKeyConstraint('meal_id', 'log_id'),
    )
    pass


def downgrade():
    pass
