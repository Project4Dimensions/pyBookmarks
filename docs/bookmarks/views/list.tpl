%# generate SQL SELECT list
  % id = row[0]
  % title = row[1]
  % uri = row[2]
  % tags = row[3]
  % note = row[4].replace('\n', '<br>\n      ')
  <div class="card mb-3">
    <div class="card-body">
      <p class="card-text text-secondary">
        <span class="text-monospace">title  &vellip;&nbsp;</span>
        {{title}}<br>
        <span class="text-monospace">uri  &nbsp;&nbsp;&vellip;&nbsp;</span>
        <!-- text-info -->
        <a href="{{uri}}" class="text-secondary">
          {{uri}}
        </a><br>
        <span class="text-monospace">tags &nbsp;&vellip;&nbsp;</span>
        {{tags}}<br>
        <span class="text-monospace">note &nbsp;&vellip;&nbsp;</span>
        {{!note}}
      </p>
      % if update_delete=='1':
      <p class="card-text text-secondary">
        <a href="/update/{{id}}" class="text-secondary">update</a> ·
        <a href="/delete/{{id}}" class="text-secondary">delete</a>
      </p>
      % end
    </div>
  </div>
