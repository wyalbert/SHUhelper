"""empty message

Revision ID: 77ee823b9fbb
Revises: 930984a48728
Create Date: 2018-04-03 16:33:35.227053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77ee823b9fbb'
down_revision = '930984a48728'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('date', sa.DateTime(), nullable=True))
    op.drop_column('order', 'month')
    op.drop_column('order', 'year')
    op.drop_column('order', 'day')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('day', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('order', sa.Column('year', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('order', sa.Column('month', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('order', 'date')
    # ### end Alembic commands ###