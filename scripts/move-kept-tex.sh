#!/bin/sh

set -eu

output_dir="${QUARTO_PROJECT_OUTPUT_DIR:-.}"

printf '%s\n' "${QUARTO_PROJECT_OUTPUT_FILES:-}" | while IFS= read -r output; do
  case "$output" in
    *.pdf)
      base_name=$(basename "$output" .pdf)
      tex_file="${base_name}.tex"

      if [ -f "$tex_file" ]; then
        mkdir -p "$output_dir"
        mv -f "$tex_file" "$output_dir/$tex_file"
      fi
      ;;
  esac
done
