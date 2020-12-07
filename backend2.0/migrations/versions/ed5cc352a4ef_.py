"""empty message

Revision ID: ed5cc352a4ef
Revises: 0feedb198686
Create Date: 2020-12-06 15:04:20.841861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed5cc352a4ef'
down_revision = '0feedb198686'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute(
        sa.sql.text(
            '''
            CREATE MATERIALIZED VIEW total_nutrition AS (
                SELECT
                    n.*,
                    food_detail.food_desc,
                    food_detail.barcode,
                    food_detail.brand,
                    json_agg(json_build_object(food_unit.unit_desc, food_unit.grams_per_unit)) AS food_units
                FROM
                    nut_per_100_gram n
                    INNER JOIN food_detail ON n.food_id = food_detail.food_id
                    INNER JOIN food_unit ON n.food_id = food_unit.food_id
                GROUP BY
                    n.food_id,
                    food_detail.food_desc,
                    food_detail.barcode,
                    food_detail.brand
            )
            '''
        )
    )
    op.create_index(op.f('ix_total_nutrition_id'), 'total_nutrition', ['food_id'], unique=True)


def downgrade():
    pass
