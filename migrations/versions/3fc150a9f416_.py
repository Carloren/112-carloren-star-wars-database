"""empty message

Revision ID: 3fc150a9f416
Revises: b48bda6e6250
Create Date: 2025-07-25 10:49:37.855518

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fc150a9f416'
down_revision = 'b48bda6e6250'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.alter_column('favorite',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.alter_column('favorite',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
