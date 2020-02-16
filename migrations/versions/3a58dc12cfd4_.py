"""empty message

Revision ID: 3a58dc12cfd4
Revises: e0d7e4726542
Create Date: 2020-02-16 09:06:29.941126

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3a58dc12cfd4'
down_revision = 'e0d7e4726542'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('service', 'admin',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False)
    op.alter_column('service', 'domain',
               existing_type=mysql.VARCHAR(length=16),
               type_=sa.String(length=32),
               existing_nullable=False)
    op.alter_column('service', 'status',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('service', 'status',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column('service', 'domain',
               existing_type=sa.String(length=32),
               type_=mysql.VARCHAR(length=16),
               existing_nullable=False)
    op.alter_column('service', 'admin',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)
    # ### end Alembic commands ###
