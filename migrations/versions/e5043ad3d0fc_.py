"""empty message

Revision ID: e5043ad3d0fc
Revises: a5cffa318ac2
Create Date: 2025-07-25 10:07:31.518119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5043ad3d0fc'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('surname', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('signup_date', sa.String(length=120), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('signup_date')
        batch_op.drop_column('surname')
        batch_op.drop_column('name')

    # ### end Alembic commands ###
