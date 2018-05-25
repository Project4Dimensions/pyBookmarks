  <div class="card mb-3">
    <div class="card-body">
      <p class="card-text text-secondary">
        <form action="{{path}}" method="GET">
          <div class="form-group">
            <input type="text" class="form-control" aria-describedby="subjectHelp"
            id="subject" name="subject" value="{{subject}}">
            <small id="subjectHelp" class="form-text text-muted">
              Subject or title (e.g., Duck test - Wikipedia)
            </small>
          </div>
          <div class="form-group">
            <input type="text" class="form-control" aria-describedby="uriHelp"
            id="uri" name="uri" value="{{uri}}">
            <small id="uriHelp" class="form-text text-muted">
              URI (e.g., https://en.wikipedia.org/wiki/Duck_test)
            </small>
          </div>
          <div class="form-group">
            <input type="text" class="form-control" aria-describedby="tagsHelp"
            id="tags" name="tags" value="{{tags}}">
            <small id="tagsHelp" class="form-text text-muted">
              Tags in lowercase (e.g., duck test wikipedia)
            </small>
          </div>
          <div class="form-group">
            <textarea class="form-control" aria-describedby="noteHelp" id="note"
            name="note" rows="2">{{note}}</textarea>
            <small id="noteHelp" class="form-text text-muted">
              Note (e.g., The duck test is a form of abductive reasoning.)
            </small>
          </div>
          <button type="submit" class="btn btn-info" name="{{name}}" value="{{name}}">
            {{label}}
          </button>
        </form>
      </p>
    </div>
  </div>
