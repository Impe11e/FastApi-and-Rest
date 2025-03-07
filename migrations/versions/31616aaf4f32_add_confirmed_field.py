"""add confirmed field

Revision ID: 31616aaf4f32
Revises: 8ab867fa9bc1
Create Date: 2025-02-25 16:44:40.584244

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '31616aaf4f32'
down_revision: Union[str, None] = '8ab867fa9bc1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    op.drop_column('users', 'сonfirmed')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('сonfirmed', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###
