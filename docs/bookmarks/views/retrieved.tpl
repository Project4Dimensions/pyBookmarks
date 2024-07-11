%# template to generate entries from SQL SELECT list
<!DOCTYPE html>
<html lang="en" class="h-100">
% include(tpl + 'head', title=title + 'retrieved')
<body class="d-flex flex-column h-100">
<main role="main" class="container mt-3 flex-shrink-0">
  % include(tpl + 'h1', h1=title + 'retrieved')
  % include(tpl + 'navigation')
  <div class="card mb-3">
    <div class="card-body">
      <p class="card-text text-secondary">
        number of entries retrieved &nbsp;&vellip;&nbsp; {{n}}
      </p>
    </div>
  </div>
  %for row in rows:
    % include(tpl + 'list', update_delete='1')
  %end
</main>
%include(tpl + 'footer')
%include(tpl + 'javascript')
</body>
</html>
