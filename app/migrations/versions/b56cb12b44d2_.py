"""empty message

Revision ID: b56cb12b44d2
Revises: 39267fd3b637
Create Date: 2021-06-08 21:52:57.169729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b56cb12b44d2'
down_revision = '39267fd3b637'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_notification_feed_to_user_id_fkey', 'user_notification_feed', type_='foreignkey')
    op.drop_constraint('user_notification_feed_from_user_id_fkey', 'user_notification_feed', type_='foreignkey')
    op.create_foreign_key(None, 'user_notification_feed', 'user_account', ['from_user_id'], ['public_id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'user_notification_feed', 'user_account', ['to_user_id'], ['public_id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_notification_feed', type_='foreignkey')
    op.drop_constraint(None, 'user_notification_feed', type_='foreignkey')
    op.create_foreign_key('user_notification_feed_from_user_id_fkey', 'user_notification_feed', 'user_account', ['from_user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('user_notification_feed_to_user_id_fkey', 'user_notification_feed', 'user_account', ['to_user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
