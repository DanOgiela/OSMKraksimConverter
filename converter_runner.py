import sys
from converter_printer import ConverterPrinter
from query_loader import ConverterQueryLoader
from converter_reader import *
from query_loader import Query

if __name__ == "__main__":
    query = Query(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    cql = ConverterQueryLoader()
    result = cql.execute_query(str(query))
    print "Kwerenda wykonana"
    converter_reader = ConverterReader(query)
    converter_reader.read_to_internal_structure(result)
    ConverterPrinter.print_to_file(sys.argv[5], converter_reader.gateways, converter_reader.junctions,
                                   converter_reader.ways)

    # for way in result.ways:
    #     print("Name: %s" % way.tags.get("name", "n/a"))
    #     print("  Highway: %s" % way.tags.get("highway", "n/a"))
    #     print("  Nodes:")
    #     for node in way.nodes:
    #         print("    Lat: %f, Lon: %f" % (node.lat, node.lon))
