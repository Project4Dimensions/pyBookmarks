<!DOCTYPE html>
<html lang="en">
% include('docs/views/head', title='Updated')

<body>
<div class="container">
  % include('docs/views/h1', h1='Updated')
  % include('docs/views/navigation')
  % include('docs/views/list', update_delete='1')
  % include('docs/views/action', action='Updated', row_id=row_id)
</div>
</body>
</html>
