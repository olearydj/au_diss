# Load necessary library
library(renv)

# Get dependencies
deps <- renv::dependencies()

# Extract unique package names from dependencies
used_packages <- unique(deps$Package)

# Get all installed packages in the renv library
library_path <- renv::paths$library()
installed_packages <- installed.packages(paths = library_path, libs_only = TRUE)[,"Package"]

# Identify packages that are installed but not used
unused_packages <- setdiff(installed_packages, used_packages)

# Exclude base and recommended packages (commonly installed with R)
base_packages <- c("base", "compiler", "datasets", "graphics", "grDevices",
                   "grid", "methods", "parallel", "splines", "stats",
                   "stats4", "tcltk", "utils", "boot", "class", "cluster",
                   "codetools", "foreign", "KernSmooth", "lattice", "MASS",
                   "Matrix", "mgcv", "nlme", "nnet", "rpart", "spatial", "survival")
packages_to_remove <- setdiff(unused_packages, base_packages)

# Print unused packages and ask user for confirmation to remove them
if (length(packages_to_remove) > 0) {
  cat("The following packages are installed but not used and will be removed:\n")
  print(packages_to_remove)
  
  # Asking for user confirmation
  response <- readline(prompt = "Do you want to proceed with removal? (yes/no): ")
  
  if (tolower(response) == "yes") {
    # Ensure packages exist before attempting to remove
    to_remove <- packages_to_remove[packages_to_remove %in% installed_packages]
    if (length(to_remove) > 0) {
      remove.packages(to_remove, lib = library_path)
      cat("Unused packages have been removed.")
    } else {
      cat("No valid packages found for removal.")
    }
  } else {
    cat("Package removal canceled by user.")
  }
} else {
  cat("No unused packages to remove.")
}
