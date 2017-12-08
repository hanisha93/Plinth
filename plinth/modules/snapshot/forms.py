#
# This file is part of Plinth.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""
Forms for snapshot module.
"""


from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class SnapshotForm(forms.Form):
  enable_timeline_snapshots = forms.BooleanField(
    label=_('Enable Timeline Snapshots'),
    required=False,
    help_text=_('When the timeline is enabled, by default a snapshot gets created once an hour.'
                ' Once a day the snapshots get cleaned up by the timeline cleanup algorithm.'))


  def clean(self):
    """Validate the form for cross-field integrity."""
    cleaned_data = super().clean()
    use_upstream_bridges = cleaned_data.get('use_upstream_bridges')
    upstream_bridges = cleaned_data.get('upstream_bridges')

    if use_upstream_bridges and not upstream_bridges:
      self.add_error('upstream_bridges', ValidationError(_(
        'Specify at least one upstream bridge to use upstream '
        'bridges.'), code='invalid'))

    return cleaned_data
