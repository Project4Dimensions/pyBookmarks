<!DOCTYPE html>
<html lang="en">
% include('docs/views/head', title='Update')

<body>
<div class="container">
  % include('docs/views/h1', h1='Update ')
  % include('docs/views/navigation')
  % include('docs/views/form', path=pth, subject=old[0], uri=old[1], tags=old[2], note=old[3], name='update_row', label='Update')
</div>
</body>
</html>
