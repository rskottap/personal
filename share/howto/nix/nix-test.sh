# Normal build
for py in 311 312 313 314; do
  nix build .#python${py}Packages.mmry
done

# Hydra-style tests
for py in 311 312 313 314; do
  nix build .#python${py}Packages.mmry.tests.pytest -L
done
