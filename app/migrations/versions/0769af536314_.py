"""empty message

Revision ID: 0769af536314
Revises: 57402fafcd49
Create Date: 2021-05-12 13:00:31.434111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0769af536314'
down_revision = '57402fafcd49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_account_preference_id_fkey', 'user_account', type_='foreignkey')
    op.drop_column('user_account', 'preference_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_account', sa.Column('preference_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('user_account_preference_id_fkey', 'user_account', 'user_preference', ['preference_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###
