import click

from cwipost import build_confusion_matrix as bcm


@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo(f"Debug mode is {'on' if debug else 'off'}")


@cli.command()
@click.option('--input-file','-i',  default='assessment.geojson', type=click.Path(exists=True), help='input data for confusion matrix')
@click.option('--output-file', '-o', default=None, show_default=True, help="Destination location for the table")
def cfm(input_file, output_file):
    output_file = 'confusion_matrix.csv' if output_file is None else output_file
    cfm = bcm.build_confustion_matrix(input_file)
    cfm.to_csv(output_file)
    