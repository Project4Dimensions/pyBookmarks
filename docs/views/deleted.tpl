<!DOCTYPE html>
<html lang="en">
% include('docs/views/head', title='Deleted')

<body>
<div class="container">
  % include('docs/views/h1', h1='Deleted')
  % include('docs/views/navigation')
  % include('docs/views/list', update_delete='0')
  % include('docs/views/action', action='Deleted', row_id=row_id)
</div>
</body>
</html>
