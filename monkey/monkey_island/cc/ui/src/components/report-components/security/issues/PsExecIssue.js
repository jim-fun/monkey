import React from 'react';
import CollapsibleWellComponent from '../CollapsibleWell';

export function psExecIssueOverview() {
  return (<li>Windows servers are configured to allow PsExec remote execution.</li>)
}

export function psExecIssueReport(issue) {
  return (
      <>
        Disable or block SMB services, disable "File and Print Sharing" or disable Admin$ share.
        <CollapsibleWellComponent>
          The machine <span className="badge badge-primary">{issue.machine}</span> (<span
          className="badge badge-info" style={{margin: '2px'}}>{issue.ip_address}</span>) was exploited via <span
          className="badge badge-danger">PsExec remoting.</span>.
          <br/>
          The attack was made possible because the target machine met all conditions for PsExec remoting and Monkey
          had access to correct credentials.
        </CollapsibleWellComponent>
      </>
    );
}
