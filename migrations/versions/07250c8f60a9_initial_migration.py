"""Initial migration.

Revision ID: 07250c8f60a9
Revises: 8c089af8822c
Create Date: 2025-04-03 23:22:28.607355

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '07250c8f60a9'
down_revision = '8c089af8822c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_address', schema=None) as batch_op:
        batch_op.alter_column('city',
               existing_type=mysql.VARCHAR(length=80),
               type_=sa.Integer(),
               existing_nullable=False)
        batch_op.alter_column('area',
               existing_type=mysql.VARCHAR(length=80),
               type_=sa.Integer(),
               existing_nullable=False)
        batch_op.create_foreign_key(None, 'area_table', ['area'], ['area_id'], onupdate='CASCADE', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'city_table', ['city'], ['city_id'], onupdate='CASCADE', ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_address', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('area',
               existing_type=sa.Integer(),
               type_=mysql.VARCHAR(length=80),
               existing_nullable=False)
        batch_op.alter_column('city',
               existing_type=sa.Integer(),
               type_=mysql.VARCHAR(length=80),
               existing_nullable=False)

    # ### end Alembic commands ###
