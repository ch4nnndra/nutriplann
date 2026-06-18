export function humanizeLabel(label) {
  return label.split('_').map(word => word.at(0).toUpperCase() + word.substring(1)).join(' ')
}