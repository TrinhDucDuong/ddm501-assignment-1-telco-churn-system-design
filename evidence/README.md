# Executed verification

Project: assignment_1

- Tests: 12 passed, 0 failed, 0 errors, 0 skipped. See pytest.txt and pytest.xml.
- Dependency validation: pip check exited 0. See pip-check.txt.
- Code validation: Ruff exited 0. See lint.txt.
- Full dataset run: 7,043 records, seed 42, 4,225/1,409/1,409 split. See pipeline.txt and summary.json.
- Actual HTTP: healthy server, valid prediction 200, invalid empty batch 422. See verification.json.
- Portability: source, data and tests copied into an unrelated temporary directory without a sibling project; tests and full training ran successfully. See portability.json.
- PDF: 11 pages, identity checked, no out-of-page text, all pages rendered and visually reviewed. See pdf-qa.json.

The Python interpreter path in verification.json points to this project's own .venv. No parent or sibling environment is required. Upstream libraries emit deprecation warnings; they are retained in the logs and are not test failures.

- Docker: image build completed, container trained its own model and responded to real HTTP requests. See docker-build.txt and docker-http.json.
