"""allow_large_files

Revision ID: 901babc6d4ff
Revises: d1f25ae779cd
Create Date: 2023-03-15 16:33:45.679217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '901babc6d4ff'
down_revision = 'd1f25ae779cd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('services', sa.Column('allow_large_files', sa.BOOLEAN(), nullable=False))
    op.drop_column('services', 'broker_url')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('services', sa.Column('broker_url', sa.TEXT(), nullable=True))
    op.drop_column('services', 'allow_large_files')
    # ### end Alembic commands ###