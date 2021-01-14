import React from 'react';
import {Card, Button} from 'react-bootstrap';

import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faCheckSquare} from '@fortawesome/free-solid-svg-icons';
import {faMinusSquare} from '@fortawesome/free-solid-svg-icons';
import {faSquare} from '@fortawesome/free-regular-svg-icons';

const MasterCheckboxState = {
  NONE: 0,
  MIXED: 1,
  ALL: 2
}

function MasterCheckbox(props) {
  const {
    title,
    disabled,
    onClick,
    checkboxState
  } = props;

  let newCheckboxIcon = faCheckSquare;

  if (checkboxState === MasterCheckboxState.NONE) {
    newCheckboxIcon = faSquare;
  } else if (checkboxState === MasterCheckboxState.MIXED) {
    newCheckboxIcon = faMinusSquare;
  }

  return (
    <Card.Header>
      <Button key={`${title}-button`} variant={'link'} disabled={disabled} onClick={onClick}>
        <FontAwesomeIcon icon={newCheckboxIcon}/>
      </Button>
      <span className={'header-title'}>{title}</span>
    </Card.Header>
  );
}

export {MasterCheckboxState, MasterCheckbox};
