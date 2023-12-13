/*
A KBase module: eapearsonWidgetDemo6
*/

module eapearsonWidgetDemo6 {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_eapearsonWidgetDemo6(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
